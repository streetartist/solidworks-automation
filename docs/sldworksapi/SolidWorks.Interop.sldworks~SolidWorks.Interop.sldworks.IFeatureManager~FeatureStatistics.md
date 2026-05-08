# FeatureStatistics Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureStatistics`

Gets statistics about the features in a part document.
Gets statistics about the features in a part document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property FeatureStatistics As FeatureStatistics
```

```

Dim instance As IFeatureManager
Dim value As FeatureStatistics
 
value = instance.FeatureStatistics
```

```

FeatureStatistics FeatureStatistics {get;}
```

```

property FeatureStatistics^ FeatureStatistics {
   FeatureStatistics^ get();
}
```

#### Property Value

[Feature statistics](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics.md)

Example

[Get Part's Feature Statistics (VB.NET)](Get_Part's_Feature_Statistics_Example_VBNET.htm)  
[Get Part's Feature Statistics (VBA)](Get_Part's_Feature_Statistics_Example_VB.htm)  
[Get Part's Feature Statistics (C#)](Get_Part's_Feature_Statistics_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
