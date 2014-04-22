try: paraview.simple
except: from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()

template_xmf = XDMFReader( FileName='/Users/ariaspg/Desktop/K3DR2/PaulGAriasParaviewTutorial/template.xmf' )

template_xmf.Sets = []
template_xmf.Grids = ['Grid_2']
template_xmf.PointArrays = ['Heat Release']

RenderView1 = GetRenderView()
RenderView1.CenterOfRotation = [127.5, 127.5, 255.5]

DataRepresentation1 = Show()
DataRepresentation1.EdgeColor = [0.0, 0.0, 0.5000076295109483]
DataRepresentation1.Slice = 255
DataRepresentation1.SelectionPointFieldDataArrayName = 'Heat Release'
DataRepresentation1.ScalarOpacityUnitDistance = 1.945432819429857
DataRepresentation1.Representation = 'Outline'
DataRepresentation1.ScaleFactor = 51.1

RenderView1.CameraViewUp = [0.2279687397853611, 0.9641805290420534, 0.13559557919364615]
RenderView1.CameraPosition = [-863.6940733467637, 447.9434085215958, -356.6440821774227]
RenderView1.OrientationAxesVisibility = 0
RenderView1.CameraClippingRange = [663.1359268351831, 1897.3525364896102]
RenderView1.CameraFocalPoint = [127.49999999999999, 127.5, 255.5]
RenderView1.CenterAxesVisibility = 0
RenderView1.CameraParallelScale = 312.71832373559437

DataRepresentation1.Representation = 'Volume'
DataRepresentation1.ColorArrayName = ('POINT_DATA', 'Heat Release')

a1_HeatRelease_PVLookupTable = GetLookupTableForArray( "Heat Release", 1, RGBPoints=[1000.0, 0.23, 0.299, 0.754, 7499.999999999998, 0.865, 0.865, 0.865, 14000.0, 0.706, 0.016, 0.15], VectorMode='Magnitude', NanColor=[0.25, 0.0, 0.0], ColorSpace='Diverging', ScalarRangeInitialized=1.0, LockScalarRange=1 )

a1_HeatRelease_PiecewiseFunction = CreatePiecewiseFunction( Points=[1000.0, 0.0, 0.5, 0.0, 14000.0, 1.0, 0.5, 0.0] )
a1_HeatRelease_PVLookupTable.ScalarOpacityFunction = a1_HeatRelease_PiecewiseFunction
DataRepresentation1.ScalarOpacityFunction = a1_HeatRelease_PiecewiseFunction
DataRepresentation1.LookupTable = a1_HeatRelease_PVLookupTable

RenderView1.ViewSize = [1200, 1200]
RenderView1.Background = [1.0, 1.0, 1.0]

Render()

WriteImage('/Users/ariaspg/Desktop/K3DR2/PaulGAriasParaviewTutorial/HR.png')
