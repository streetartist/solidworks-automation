# Next Method (IEnumBodies)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies~Next`

Obsolete. Superseded by IEnumBodies2::Next.
Obsolete. Superseded by [IEnumBodies2::Next](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies2~Next.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Next( _
   ByVal Celt As System.Integer, _
   ByRef Rgelt As Body, _
   ByRef PceltFetched As System.Integer _
) 
```

```

Dim instance As IEnumBodies
Dim Celt As System.Integer
Dim Rgelt As Body
Dim PceltFetched As System.Integer
 
instance.Next(Celt, Rgelt, PceltFetched)
```

```

void Next( 
   System.int Celt,
   out Body Rgelt,
   out System.int PceltFetched
)
```

```

void Next( 
   System.int Celt,
   [Out] Body^ Rgelt,
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

[IEnumBodies Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies.md)  
[IEnumBodies Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies_members.md)
