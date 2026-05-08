# GetBoundingBoxDirection1 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~GetBoundingBoxDirection1`

Gets bounding box direction 1 (top manipulator for both linear and radial slicing).
Gets bounding box direction 1 (top manipulator for both linear and radial slicing).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBoundingBoxDirection1() As System.Double
```

```

Dim instance As ISlicingData
Dim value As System.Double
 
value = instance.GetBoundingBoxDirection1()
```

```

System.double GetBoundingBoxDirection1()
```

```

System.double GetBoundingBoxDirection1(); 
```

#### Return Value

0.0 < top manipulator < 500.0

Remarks

This method is only valid after you have pre-selected the first slicing plane.

Use these methods to get the slicing volume for including or excluding geometry for slicing:

- ISlicingData::GetBoundingBoxDirection1
- [ISlicingData::GetBoundingBoxDirection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~GetBoundingBoxDirection2.md)
- [ISlicingData::GetBoundingBoxDirection3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~GetBoundingBoxDirection3.md)
- [ISlicingData::GetBoundingBoxDirection4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~GetBoundingBoxDirection4.md)

Example

See the [ISlicingData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISlicingData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.md)  
[ISlicingData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData_members.md)  
[ISlicingData::SetBoundingBoxDirection1 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~SetBoundingBoxDirection1.md)
