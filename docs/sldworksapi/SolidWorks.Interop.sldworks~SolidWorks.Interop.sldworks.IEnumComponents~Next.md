# Next Method (IEnumComponents)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumComponents~Next`

Obsolete. Superseded by IEnumComponents2::Next.
Obsolete. Superseded by [IEnumComponents2::Next](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumComponents2~Next.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Next( _
   ByVal Celt As System.Integer, _
   ByRef Rgelt As Component, _
   ByRef PceltFetched As System.Integer _
) 
```

```

Dim instance As IEnumComponents
Dim Celt As System.Integer
Dim Rgelt As Component
Dim PceltFetched As System.Integer
 
instance.Next(Celt, Rgelt, PceltFetched)
```

```

void Next( 
   System.int Celt,
   out Component Rgelt,
   out System.int PceltFetched
)
```

```

void Next( 
   System.int Celt,
   [Out] Component^ Rgelt,
   [Out] System.int PceltFetched
) 
```

#### Parameters

*Celt*

*Rgelt*

*PceltFetched*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnumComponents Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumComponents.md)  
[IEnumComponents Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumComponents_members.md)
