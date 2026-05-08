# GetPartingSurfacesCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~GetPartingSurfacesCount`

Gets the number of parting surface bodies in this tooling split feature.
Gets the number of parting surface bodies in this tooling split feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPartingSurfacesCount() As System.Integer
```

```

Dim instance As IToolingSplitFeatureData
Dim value As System.Integer
 
value = instance.GetPartingSurfacesCount()
```

```

System.int GetPartingSurfacesCount()
```

```

System.int GetPartingSurfacesCount(); 
```

#### Return Value

Number of parting surface bodies

Remarks

Call this method before calling [IToolingSplitFeatureData::IGetPartingSurfaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~IGetPartingSurfaces.md) to get the size of the array for that method.

Example

See the [IToolingSplitFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IToolingSplitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData.md)  
[IToolingSplitFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData_members.md)  
[IToolingSplitFeatureData::ISetPartingSurfaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~ISetPartingSurfaces.md)  
[IToolingSplitFeatureData::PartingSurfaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~PartingSurfaces.md)
