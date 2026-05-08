# Next Method (IEnumFaces2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumFaces2~Next`

Gets the next face in the faces enumeration.
Gets the next face in the faces enumeration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Next( _
   ByVal Celt As System.Integer, _
   ByRef Rgelt As Face2, _
   ByRef PceltFetched As System.Integer _
) 
```

```

Dim instance As IEnumFaces2
Dim Celt As System.Integer
Dim Rgelt As Face2
Dim PceltFetched As System.Integer
 
instance.Next(Celt, Rgelt, PceltFetched)
```

```

void Next( 
   System.int Celt,
   out Face2 Rgelt,
   out System.int PceltFetched
)
```

```

void Next( 
   System.int Celt,
   [Out] Face2^ Rgelt,
   [Out] System.int PceltFetched
) 
```

#### Parameters

*Celt*
:   Number of faces for the faces enumeration

*Rgelt*
:   Pointer to an array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) of size Celt

*PceltFetched*
:   Pointer to the number of faces returned from the list; this value can be less than Celt if you asked for more faces than exist, or it can be NULL if no more faces exist

Remarks

For use in in-process DLLs only.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnumFaces2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumFaces2.md)  
[IEnumFaces2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumFaces2_members.md)
