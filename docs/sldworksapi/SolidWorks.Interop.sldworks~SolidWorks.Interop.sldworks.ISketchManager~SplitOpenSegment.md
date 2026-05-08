# SplitOpenSegment Method (ISketchManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SplitOpenSegment`

Splits the selected open sketch segment into two sketch segments.
Splits the selected open sketch segment into two sketch segments.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SplitOpenSegment( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Object
```

```

Dim instance As ISketchManager
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Object
 
value = instance.SplitOpenSegment(X, Y, Z)
```

```

System.object SplitOpenSegment( 
   System.double X,
   System.double Y,
   System.double Z
)
```

```

System.Object^ SplitOpenSegment( 
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*X*
:   X coordinate of the point that splits the sketch segment in two

*Y*
:   Y coordinate of the point that splits the sketch segment in two

*Z*
:   Z coordinate of the point that splits the sketch segment in two

#### Return Value

Array of [sketch segments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md) of the now split formerly open sketch skegment

Remarks

Before calling this method, be sure to disable snapping by either:

- De-selecting **System Options > Sketch > Relations/Snaps > Enable snapping**

    - or -

- Calling [ISldWorks::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.md)([swUserPreferenceToggle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceToggle_e.html).swSketchInference, false).

Example

[Split Open Sketch Segment (VBA)](Split_Open_Sketch_Segment_Example_VB.htm)  
[Split Open Sketch Segment (VB.NET)](Split_Open_Sketch_Segment_Example_VBNET.htm)  
[Split Open Sketch Segment (C#)](Split_Open_Sketch_Segment_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)  
[ISketchManager::SplitClosedSegment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SplitClosedSegment.md)
