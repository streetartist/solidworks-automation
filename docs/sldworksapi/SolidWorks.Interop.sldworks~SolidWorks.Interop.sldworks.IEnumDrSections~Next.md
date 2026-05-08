# Next Method (IEnumDrSections)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDrSections~Next`

Gets the next section view in the section views enumeration.
Gets the next section view in the section views enumeration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Next( _
   ByVal Celt As System.Integer, _
   ByRef Rgelt As DrSection, _
   ByRef PceltFetched As System.Integer _
) 
```

```

Dim instance As IEnumDrSections
Dim Celt As System.Integer
Dim Rgelt As DrSection
Dim PceltFetched As System.Integer
 
instance.Next(Celt, Rgelt, PceltFetched)
```

```

void Next( 
   System.int Celt,
   out DrSection Rgelt,
   out System.int PceltFetched
)
```

```

void Next( 
   System.int Celt,
   [Out] DrSection^ Rgelt,
   [Out] System.int PceltFetched
) 
```

#### Parameters

*Celt*
:   Number of section views for the section views enumeration

*Rgelt*
:   Pointer to an array of [section views](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.md) of size Celt

*PceltFetched*
:   Pointer to the number of drawing sections returned from the list; this value can be less than Celt if you ask for more drawing sections than exist, or it can be NULL if no more drawing sections exist

Remarks

For use in in-process DLLs only.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnumDrSections Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDrSections.md)  
[IEnumDrSections Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDrSections_members.md)
