# GetFeature Method (ISimulation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation~GetFeature`

Obsolete. Not superseded.
Obsolete. Not superseded.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFeature() As Feature
```

```

Dim instance As ISimulation
Dim value As Feature
 
value = instance.GetFeature()
```

```

Feature GetFeature()
```

```

Feature^ GetFeature(); 
```

#### Return Value

[Feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

After using this method to get the feature, use either of the following methods to get the [ISimulation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation.md) interface:

- [IFeature::GetSpecificFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.md)
- [IAssemblyDoc::GetSimulation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetSimulation.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation.md)  
[ISimulation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation_members.md)
