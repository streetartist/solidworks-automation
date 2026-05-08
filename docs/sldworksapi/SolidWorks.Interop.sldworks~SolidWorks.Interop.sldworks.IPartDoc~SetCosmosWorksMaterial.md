# SetCosmosWorksMaterial Method (IPartDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetCosmosWorksMaterial`

Assigns the material to use during analysis to this part.
Assigns the material to use during analysis to this part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetCosmosWorksMaterial( _
   ByVal ConfigName As System.String, _
   ByVal Type As System.Integer _
) 
```

```

Dim instance As IPartDoc
Dim ConfigName As System.String
Dim Type As System.Integer
 
instance.SetCosmosWorksMaterial(ConfigName, Type)
```

```

void SetCosmosWorksMaterial( 
   System.string ConfigName,
   System.int Type
)
```

```

void SetCosmosWorksMaterial( 
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

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IComponent2::SetCosmosWorksMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetCosmosWorksMaterial.md)
