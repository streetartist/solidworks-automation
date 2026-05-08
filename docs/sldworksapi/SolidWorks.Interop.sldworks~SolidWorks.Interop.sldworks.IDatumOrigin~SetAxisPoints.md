# SetAxisPoints Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin~SetAxisPoints`

Sets the points that define the geometry of this datum origin.
Sets the points that define the geometry of this datum origin.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetAxisPoints( _
   ByVal PointData As System.Object _
) As System.Boolean
```

```

Dim instance As IDatumOrigin
Dim PointData As System.Object
Dim value As System.Boolean
 
value = instance.SetAxisPoints(PointData)
```

```

System.bool SetAxisPoints( 
   System.object PointData
)
```

```

System.bool SetAxisPoints( 
   System.Object^ PointData
) 
```

#### Parameters

*PointData*
:   Array of 4 doubles (see [Remarks](#Remarks))

Remarks

This method gives you control over the shape of the symbol.

The array of 4 doubles is 2 (X,Y) coordinates in drawing space:

- The first coordinate (array items 0 and 1) is the tip of the arrowhead on the X leader portion of the symbol.
- The second coordinate (array items 2 and 3) is the tip of the arrowhead on the Y leader portion of the symbol.

The interactive user has this control via the selection drag handles of the symbol.

This method returns a BOOLEAN indicating success or failure of the operation. The operation can fail if either of the coordinates is so close to the symbol origin that the symbol cannot be drawn properly.  There must be:

- Room to draw the arrow at the end of the origin leaders
- A gap between the symbol origin and the beginning of the first leader.

You can get:

- Coordinates of the symbol origin using [IAnnotation::GetPosition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPosition.md).
- Arrowhead length using [IModelDocExtension::GetUserPreferenceDouble](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceDouble.md) - swDetailingArrowWidth
- Gap using IModelDocExtension::GetUserPreferenceDouble - swDetailingWitnessLineGap

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDatumOrigin Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin.md)  
[IDatumOrigin Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin_members.md)  
[IDatumOrigin::ISetAxisPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin~ISetAxisPoints.md)  
[IDatumOrigin::IGetAxisPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin~IGetAxisPoints2.md)  
[IDatumOrigin::GetAxisPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin~GetAxisPoints2.md)
