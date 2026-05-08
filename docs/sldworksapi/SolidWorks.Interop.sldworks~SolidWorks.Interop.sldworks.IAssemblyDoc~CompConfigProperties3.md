# CompConfigProperties3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CompConfigProperties3`

Obsolete. Superseded by IAssemblyDoc::CompConfigProperties4.
Obsolete. Superseded by [IAssemblyDoc::CompConfigProperties4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CompConfigProperties4.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CompConfigProperties3( _
   ByVal Suppression As System.Integer, _
   ByVal Solving As System.Integer, _
   ByVal Visibility As System.Boolean, _
   ByVal FeatureDetails As System.Boolean _
) As System.Boolean
```

```

Dim instance As IAssemblyDoc
Dim Suppression As System.Integer
Dim Solving As System.Integer
Dim Visibility As System.Boolean
Dim FeatureDetails As System.Boolean
Dim value As System.Boolean
 
value = instance.CompConfigProperties3(Suppression, Solving, Visibility, FeatureDetails)
```

```

System.bool CompConfigProperties3( 
   System.int Suppression,
   System.int Solving,
   System.bool Visibility,
   System.bool FeatureDetails
)
```

```

System.bool CompConfigProperties3( 
   System.int Suppression,
   System.int Solving,
   System.bool Visibility,
   System.bool FeatureDetails
) 
```

#### Parameters

*Suppression*

*Solving*

*Visibility*

*FeatureDetails*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)
