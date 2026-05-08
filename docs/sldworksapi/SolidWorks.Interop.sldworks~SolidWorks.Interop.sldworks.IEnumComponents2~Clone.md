# Clone Method (IEnumComponents2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumComponents2~Clone`

Clones the components enumeration.
Clones the components enumeration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Clone( _
   ByRef Ppenum As EnumComponents2 _
) 
```

```

Dim instance As IEnumComponents2
Dim Ppenum As EnumComponents2
 
instance.Clone(Ppenum)
```

```

void Clone( 
   out EnumComponents2 Ppenum
)
```

```

void Clone( 
   [Out] EnumComponents2^ Ppenum
) 
```

#### Parameters

*Ppenum*
:   Pointer to the cloned [components enumeraton](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumComponents2.md)

Remarks

For use in in-process DLLs only.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnumComponents2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumComponents2.md)  
[IEnumComponents2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumComponents2_members.md)
