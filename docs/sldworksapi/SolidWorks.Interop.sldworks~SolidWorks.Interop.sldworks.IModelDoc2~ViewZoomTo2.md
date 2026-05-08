# ViewZoomTo2 Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewZoomTo2`

Zooms to the specified region.
Zooms to the specified region.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ViewZoomTo2( _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal Z1 As System.Double, _
   ByVal X2 As System.Double, _
   ByVal Y2 As System.Double, _
   ByVal Z2 As System.Double _
) 
```

```

Dim instance As IModelDoc2
Dim X1 As System.Double
Dim Y1 As System.Double
Dim Z1 As System.Double
Dim X2 As System.Double
Dim Y2 As System.Double
Dim Z2 As System.Double
 
instance.ViewZoomTo2(X1, Y1, Z1, X2, Y2, Z2)
```

```

void ViewZoomTo2( 
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2
)
```

```

void ViewZoomTo2( 
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2
) 
```

#### Parameters

*X1*
:   X value for the lower-left point of the zoom area

*Y1*
:   Y value for the lower- left point of the zoom area

*Z1*
:   Z value for the lower-left point of the zoom area

*X2*
:   X value for the upper-right point of the zoom area

*Y2*
:   Y value for the upper-right point of the zoom area

*Z2*
:   Z value for the upper-right point of the zoom area

Example

[Zoom To Region (VBA)](Zoom_to_Region_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::ViewZoomin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewZoomin.md)  
[IModelDoc2::ViewZoomout Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewZoomout.md)  
[IModelDoc2::ViewZoomto Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewZoomto.md)  
[IModelDoc2::ViewZoomtofit2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewZoomtofit2.md)  
[IModelDoc2::ViewZoomToSelection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewZoomToSelection.md)  
[IModelDoc2::ViewOrientationUndo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewOrientationUndo.md)  
[IModelDoc2::ViewRotate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewRotate.md)  
[IModelDoc2::ViewRotateminusx Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewRotateminusx.md)  
[IModelDoc2::ViewRotateminusy Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewRotateminusy.md)  
[IModelDoc2::ViewRotateminusz Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewRotateminusz.md)  
[IModelDoc2::ViewRotateplusx Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewRotateplusx.md)  
[IModelDoc2::ViewRotateplusy Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewRotateplusy.md)  
[IModelDoc2::ViewRotateplusz Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewRotateplusz.md)  
[IModelDoc2::ViewRotXMinusNinety Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewRotXMinusNinety.md)  
[IModelDoc2::ViewRotXPlusNinety Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewRotXPlusNinety.md)  
[IModelDoc2::ViewRotYMinusNinety Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewRotYMinusNinety.md)  
[IModelDoc2::ViewRotYPlusNinety Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewRotYPlusNinety.md)  
[IModelDocExtension::ViewZoomToSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ViewZoomToSheet.md)
