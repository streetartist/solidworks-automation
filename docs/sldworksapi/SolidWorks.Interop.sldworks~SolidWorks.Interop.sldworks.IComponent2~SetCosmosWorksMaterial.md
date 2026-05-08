# SetCosmosWorksMaterial Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetCosmosWorksMaterial`

Assigns the material to use during analysis to this component.
Assigns the material to use during analysis to this component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetCosmosWorksMaterial( _
   ByVal ConfigName As System.String, _
   ByVal Type As System.Integer _
) As System.Boolean
```

```

Dim instance As IComponent2
Dim ConfigName As System.String
Dim Type As System.Integer
Dim value As System.Boolean
 
value = instance.SetCosmosWorksMaterial(ConfigName, Type)
```

```

System.bool SetCosmosWorksMaterial( 
   System.string ConfigName,
   System.int Type
)
```

```

System.bool SetCosmosWorksMaterial( 
   System.String^ ConfigName,
   System.int Type
) 
```

#### Parameters

*ConfigName*
:   Name of the configuration

*Type*
:   Type of material to assign as defined by [swCosmosWorksMat](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCosmosWorksMat.html)

#### Return Value

True if the material is assigned, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IPartDoc::SetCosmosWorksMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetCosmosWorksMaterial.md)
