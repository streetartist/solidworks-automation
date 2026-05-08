# GetComponentsCount Method (ICavityFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~GetComponentsCount`

Gets the number of design components in this cavity feature.
Gets the number of design components in this cavity feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetComponentsCount() As System.Integer
```

```

Dim instance As ICavityFeatureData
Dim value As System.Integer
 
value = instance.GetComponentsCount()
```

```

System.int GetComponentsCount()
```

```

System.int GetComponentsCount(); 
```

Remarks

Call this method before calling [ICavityFeatureData::IGetComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~IGetComponents.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICavityFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData.md)  
[ICavityFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData_members.md)  
[ICavityFeatureData::ISetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~ISetComponents.md)  
[ICavityFeatureData::Components Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~Components.md)
