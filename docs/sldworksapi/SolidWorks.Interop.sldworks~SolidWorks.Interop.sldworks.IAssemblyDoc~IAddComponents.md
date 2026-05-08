# IAddComponents Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IAddComponents`

Obsolete. Superseded by IAssemblyDoc::IAddComponents2.
Obsolete. Superseded by [IAssemblyDoc::IAddComponents2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IAddComponents2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IAddComponents( _
   ByRef Count As System.Integer, _
   ByRef Names As System.String, _
   ByRef Transforms As System.Double _
) As Component
```

```

Dim instance As IAssemblyDoc
Dim Count As System.Integer
Dim Names As System.String
Dim Transforms As System.Double
Dim value As Component
 
value = instance.IAddComponents(Count, Names, Transforms)
```

```

Component IAddComponents( 
   ref System.int Count,
   ref System.string Names,
   ref System.double Transforms
)
```

```

Component^ IAddComponents( 
   System.int% Count,
   System.String^% Names,
   System.double% Transforms
) 
```

#### Parameters

*Count*

*Names*

*Transforms*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)
