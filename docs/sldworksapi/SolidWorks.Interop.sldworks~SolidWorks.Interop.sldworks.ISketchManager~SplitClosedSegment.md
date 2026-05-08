# SplitClosedSegment Method (ISketchManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SplitClosedSegment`

Splits the selected closed sketch segment into two sketch segments.
Splits the selected closed sketch segment into two sketch segments.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SplitClosedSegment( _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal Z1 As System.Double, _
   ByVal X2 As System.Double, _
   ByVal Y2 As System.Double, _
   ByVal Z2 As System.Double _
) As System.Object
```

```

Dim instance As ISketchManager
Dim X1 As System.Double
Dim Y1 As System.Double
Dim Z1 As System.Double
Dim X2 As System.Double
Dim Y2 As System.Double
Dim Z2 As System.Double
Dim value As System.Object
 
value = instance.SplitClosedSegment(X1, Y1, Z1, X2, Y2, Z2)
```

```

System.object SplitClosedSegment( 
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2
)
```

```

System.Object^ SplitClosedSegment( 
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
:   X coordinate of first point

*Y1*
:   Y coordinate of first point

*Z1*
:   Z coordinate of first point

*X2*
:   X coordinate of second point

*Y2*
:   Y coordinate of second point

*Z2*
:   Z coordinate of second point

#### Return Value

Array of [sketch segments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md) of the now split formerly closed sketch skegment

Remarks

Before calling this method, be sure to disable snapping by either:

- De-selecting **System Options > Sketch > Relations/Snaps > Enable snapping**

    - or -

- Calling [ISldWorks::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.md)([swUserPreferenceToggle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceToggle_e.html).swSketchInference, false).

Example

[Split Closed Sketch Segment (VBA)](Split_Closed_Sketch_Segment_Example_VB.htm)  
[Split Closed Sketch Segment (VB.NET)](Split_Closed_Sketch_Segment_Example_VBNET.htm)  
[Split Closed Sketch Segment (C#)](Split_Closed_Sketch_Segment_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)  
[ISketchManager::SplitOpenSegment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SplitOpenSegment.md)
