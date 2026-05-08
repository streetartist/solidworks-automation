# Clone Method (IEnumComponents)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumComponents~Clone`

Obsolete. Superseded by IEnumComponents2::Clone.
Obsolete. Superseded by [IEnumComponents2::Clone](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumComponents2~Clone.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Clone( _
   ByRef Ppenum As EnumComponents _
) 
```

```

Dim instance As IEnumComponents
Dim Ppenum As EnumComponents
 
instance.Clone(Ppenum)
```

```

void Clone( 
   out EnumComponents Ppenum
)
```

```

void Clone( 
   [Out] EnumComponents^ Ppenum
) 
```

#### Parameters

*Ppenum*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnumComponents Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumComponents.md)  
[IEnumComponents Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumComponents_members.md)
