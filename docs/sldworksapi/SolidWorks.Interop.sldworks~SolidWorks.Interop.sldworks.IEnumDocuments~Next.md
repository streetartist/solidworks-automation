# Next Method (IEnumDocuments)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDocuments~Next`

Obsolete. Superseded by IEnumDocuments2::Next.
Obsolete. Superseded by [IEnumDocuments2::Next](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDocuments2~Next.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Next( _
   ByVal Celt As System.Integer, _
   ByRef Rgelt As ModelDoc, _
   ByRef PceltFetched As System.Integer _
) 
```

```

Dim instance As IEnumDocuments
Dim Celt As System.Integer
Dim Rgelt As ModelDoc
Dim PceltFetched As System.Integer
 
instance.Next(Celt, Rgelt, PceltFetched)
```

```

void Next( 
   System.int Celt,
   out ModelDoc Rgelt,
   out System.int PceltFetched
)
```

```

void Next( 
   System.int Celt,
   [Out] ModelDoc^ Rgelt,
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

[IEnumDocuments Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDocuments.md)  
[IEnumDocuments Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDocuments_members.md)
