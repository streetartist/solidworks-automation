# SetBoundingBoxDirection1 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~SetBoundingBoxDirection1`

Sets bounding box direction 1 (top manipulator for both linear and radial slicing).
Sets bounding box direction 1 (top manipulator for both linear and radial slicing).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetBoundingBoxDirection1( _
   ByVal Direction As System.Double _
) As System.Boolean
```

```

Dim instance As ISlicingData
Dim Direction As System.Double
Dim value As System.Boolean
 
value = instance.SetBoundingBoxDirection1(Direction)
```

```

System.bool SetBoundingBoxDirection1( 
   System.double Direction
)
```

```

System.bool SetBoundingBoxDirection1( 
   System.double Direction
) 
```

#### Parameters

*Direction*
:   0.0 < top manipulator < 500.0 (see **Remarks**)

#### Return Value

True if direction 1 of bounding box successfully set, false if not

Remarks

Use these methods to adjust the slicing volume to include or exclude geometry for slicing:

- ISlicingData::SetBoundingBoxDirection1
- [ISlicingData::SetBoundingBoxDirection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~SetBoundingBoxDirection2.md)
- [ISlicingData::SetBoundingBoxDirection3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~SetBoundingBoxDirection3.md)
- [ISlicingData::SetBoundingBoxDirection4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~SetBoundingBoxDirection4.md)

This method fails when:

- Direction exceeds the specified limits.
- The bounding box cannot be created because [ISlicingData::PlaneReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~PlaneReferences.md) has not been set.

Example

See the [ISlicingData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISlicingData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.md)  
[ISlicingData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData_members.md)  
[ISlicingData::GetBoundingBoxDirection1 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~GetBoundingBoxDirection1.md)
