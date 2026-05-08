# GetBoundingBoxDirection4 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~GetBoundingBoxDirection4`

Gets bounding box direction 4 (bottom manipulator for linear slicing, outer radius for radial slicing).
Gets bounding box direction 4 (bottom manipulator for linear slicing, outer radius for radial slicing).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBoundingBoxDirection4() As System.Double
```

```

Dim instance As ISlicingData
Dim value As System.Double
 
value = instance.GetBoundingBoxDirection4()
```

```

System.double GetBoundingBoxDirection4()
```

```

System.double GetBoundingBoxDirection4(); 
```

#### Return Value

For linear slicing:

    -500.0 < bottom manipulator < 0

For radial slicing:

    Inner radius < outer radius < user-interface maximum for this case

Remarks

This method is only valid after you have pre-selected the first slicing plane.

Use these methods to get the slicing volume for including or excluding geometry for slicing:

- [ISlicingData::GetBoundingBoxDirection1](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~GetBoundingBoxDirection1.md)
- [ISlicingData::GetBoundingBoxDirection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~GetBoundingBoxDirection2.md)
- [ISlicingData::GetBoundingBoxDirection3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~GetBoundingBoxDirection3.md)
- ISlicingData::GetBoundingBoxDirection4

Example

See the [ISlicingData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISlicingData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.md)  
[ISlicingData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData_members.md)  
[ISlicingData::SetBoundingBoxDirection4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~SetBoundingBoxDirection4.md)
