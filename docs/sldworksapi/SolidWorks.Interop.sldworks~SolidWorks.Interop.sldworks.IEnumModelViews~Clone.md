# Clone Method (IEnumModelViews)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumModelViews~Clone`

Clones the model views enumeration.
Clones the model views enumeration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Clone( _
   ByRef Ppenum As EnumModelViews _
) 
```

```

Dim instance As IEnumModelViews
Dim Ppenum As EnumModelViews
 
instance.Clone(Ppenum)
```

```

void Clone( 
   out EnumModelViews Ppenum
)
```

```

void Clone( 
   [Out] EnumModelViews^ Ppenum
) 
```

#### Parameters

*Ppenum*
:   Pointer to the model views enumeration

Remarks

For use in in-process DLLs only.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnumModelViews Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumModelViews.md)  
[IEnumModelViews Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumModelViews_members.md)
