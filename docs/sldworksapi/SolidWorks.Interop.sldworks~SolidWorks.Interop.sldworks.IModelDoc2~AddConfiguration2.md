# AddConfiguration2 Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddConfiguration2`

Obsolete. Superseded by IModelDoc2::AddConfiguration3.
Obsolete. Superseded by [IModelDoc2::AddConfiguration3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddConfiguration3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddConfiguration2( _
   ByVal Name As System.String, _
   ByVal Comment As System.String, _
   ByVal AlternateName As System.String, _
   ByVal SuppressByDefault As System.Boolean, _
   ByVal HideByDefault As System.Boolean, _
   ByVal MinFeatureManager As System.Boolean, _
   ByVal InheritProperties As System.Boolean, _
   ByVal Flags As System.UInteger _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim Name As System.String
Dim Comment As System.String
Dim AlternateName As System.String
Dim SuppressByDefault As System.Boolean
Dim HideByDefault As System.Boolean
Dim MinFeatureManager As System.Boolean
Dim InheritProperties As System.Boolean
Dim Flags As System.UInteger
Dim value As System.Boolean
 
value = instance.AddConfiguration2(Name, Comment, AlternateName, SuppressByDefault, HideByDefault, MinFeatureManager, InheritProperties, Flags)
```

```

System.bool AddConfiguration2( 
   System.string Name,
   System.string Comment,
   System.string AlternateName,
   System.bool SuppressByDefault,
   System.bool HideByDefault,
   System.bool MinFeatureManager,
   System.bool InheritProperties,
   System.uint Flags
)
```

```

System.bool AddConfiguration2( 
   System.String^ Name,
   System.String^ Comment,
   System.String^ AlternateName,
   System.bool SuppressByDefault,
   System.bool HideByDefault,
   System.bool MinFeatureManager,
   System.bool InheritProperties,
   System.uint Flags
) 
```

#### Parameters

*Name*

*Comment*

*AlternateName*

*SuppressByDefault*

*HideByDefault*

*MinFeatureManager*

*InheritProperties*

*Flags*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
