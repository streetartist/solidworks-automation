# ReplacePLMComponents Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReplacePLMComponents`

Replaces a selected SOLIDWORKS Connected component in this assembly with the specified component from a 3DEXPERIENCE collaborative space.
Replaces a selected [SOLIDWORKS Connected](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm) component in this assembly with the specified component from a 3DEXPERIENCE collaborative space.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ReplacePLMComponents( _
   ByVal PLMID As System.String, _
   ByVal ConfigName As System.String, _
   ByVal ReplaceAllInstance As System.Boolean, _
   ByVal UseConfigChoice As System.Integer, _
   ByVal ReAttachMates As System.Boolean _
) As System.Boolean
```

```

Dim instance As IAssemblyDoc
Dim PLMID As System.String
Dim ConfigName As System.String
Dim ReplaceAllInstance As System.Boolean
Dim UseConfigChoice As System.Integer
Dim ReAttachMates As System.Boolean
Dim value As System.Boolean
 
value = instance.ReplacePLMComponents(PLMID, ConfigName, ReplaceAllInstance, UseConfigChoice, ReAttachMates)
```

```

System.bool ReplacePLMComponents( 
   System.string PLMID,
   System.string ConfigName,
   System.bool ReplaceAllInstance,
   System.int UseConfigChoice,
   System.bool ReAttachMates
)
```

```

System.bool ReplacePLMComponents( 
   System.String^ PLMID,
   System.String^ ConfigName,
   System.bool ReplaceAllInstance,
   System.int UseConfigChoice,
   System.bool ReAttachMates
) 
```

#### Parameters

*PLMID*
:   Unique ID of a replacement component in the collaboration space

*ConfigName*
:   Name of a configuration (Physical Product) in the replacement component; an empty string indicates the default configuration of the replacement component

*ReplaceAllInstance*
:   True to replace all instances of the selected components with the replacement component, false to not

*UseConfigChoice*
:   Configuration to use as defined in [swReplaceComponentsConfiguration\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swReplaceComponentsConfiguration_e.html)

*ReAttachMates*
:   True to reattach any existing mates to the replacement component, false to not

#### Return Value

True if the selected component is replaced, false if not

Remarks

Before calling this method, save any components that have been modified in this assembly. This method closes any open component files without saving modifications.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::AddPLMComponent Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddPLMComponent.md)
