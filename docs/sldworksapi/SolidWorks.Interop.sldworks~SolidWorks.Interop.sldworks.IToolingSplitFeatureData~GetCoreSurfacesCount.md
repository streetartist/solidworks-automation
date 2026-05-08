# GetCoreSurfacesCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~GetCoreSurfacesCount`

Gets the number of core surface bodies in this tooling split feature.
Gets the number of core surface bodies in this tooling split feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCoreSurfacesCount() As System.Integer
```

```

Dim instance As IToolingSplitFeatureData
Dim value As System.Integer
 
value = instance.GetCoreSurfacesCount()
```

```

System.int GetCoreSurfacesCount()
```

```

System.int GetCoreSurfacesCount(); 
```

#### Return Value

Number of core surface bodies

Remarks

Call this method before calling [IToolingSplitFeatureData::IGetCoreSurfaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~IGetCoreSurfaces.md) to get the size of the array for that method.

Example

See the [IToolingSplitFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IToolingSplitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData.md)  
[IToolingSplitFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData_members.md)  
[IToolingSplitFeatureData::ISetCoreSurfaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~ISetCoreSurfaces.md)  
[IToolingSplitFeatureData::CoreSurfaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~CoreSurfaces.md)
