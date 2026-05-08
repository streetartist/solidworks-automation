# SaveAs4 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SaveAs4`

Obsolete. Superseded by IModelDocExtension::SaveAs.
Obsolete. Superseded by [IModelDocExtension::SaveAs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveAs.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SaveAs4( _
   ByVal Name As System.String, _
   ByVal Version As System.Integer, _
   ByVal Options As System.Integer, _
   ByRef Errors As System.Integer, _
   ByRef Warnings As System.Integer _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim Name As System.String
Dim Version As System.Integer
Dim Options As System.Integer
Dim Errors As System.Integer
Dim Warnings As System.Integer
Dim value As System.Boolean
 
value = instance.SaveAs4(Name, Version, Options, Errors, Warnings)
```

```

System.bool SaveAs4( 
   System.string Name,
   System.int Version,
   System.int Options,
   out System.int Errors,
   out System.int Warnings
)
```

```

System.bool SaveAs4( 
   System.String^ Name,
   System.int Version,
   System.int Options,
   [Out] System.int Errors,
   [Out] System.int Warnings
) 
```

#### Parameters

*Name*

*Version*

*Options*

*Errors*

*Warnings*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
