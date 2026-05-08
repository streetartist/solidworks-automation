# CompConfigProperties Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CompConfigProperties`

Obsolete. Superseded by IAssemblyDoc::CompConfigProperties4.
Obsolete. Superseded by [IAssemblyDoc::CompConfigProperties4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CompConfigProperties4.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub CompConfigProperties( _
   ByVal M_suppressed As System.Boolean, _
   ByVal M_show_component As System.Boolean, _
   ByVal M_fdetail As System.Boolean _
) 
```

```

Dim instance As IAssemblyDoc
Dim M_suppressed As System.Boolean
Dim M_show_component As System.Boolean
Dim M_fdetail As System.Boolean
 
instance.CompConfigProperties(M_suppressed, M_show_component, M_fdetail)
```

```

void CompConfigProperties( 
   System.bool M_suppressed,
   System.bool M_show_component,
   System.bool M_fdetail
)
```

```

void CompConfigProperties( 
   System.bool M_suppressed,
   System.bool M_show_component,
   System.bool M_fdetail
) 
```

#### Parameters

*M\_suppressed*

*M\_show\_component*

*M\_fdetail*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)
