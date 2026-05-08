# TableType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~TableType`

Gets and sets the type of table for the Bill of Materials.
Gets and sets the type of table for the Bill of Materials.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TableType As System.Integer
```

```

Dim instance As IBomFeature
Dim value As System.Integer
 
instance.TableType = value
 
value = instance.TableType
```

```

System.int TableType {get; set;}
```

```

property System.int TableType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of table for the Bill of Materials as defined in [swBomType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBomType_e.html)

Example

See [IBomFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.md)  
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.md)  
[IBomFeature::Configuration Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~Configuration.md)  
[IBomFeature::GetConfigurationCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~GetConfigurationCount.md)  
[IBomFeature::GetConfigurations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~GetConfigurations.md)  
[IBomFeature::IGetConfigurations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~IGetConfigurations.md)  
[IBomFeature::SetConfigurations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~SetConfigurations.md)  
[IBomFeature::ISetConfigurations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~ISetConfigurations.md)  
[IBomFeature::DetailedCutList Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~DetailedCutList.md)
