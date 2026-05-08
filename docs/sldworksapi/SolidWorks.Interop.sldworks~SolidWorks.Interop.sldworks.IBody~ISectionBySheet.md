# ISectionBySheet Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~ISectionBySheet`

Obsolete. Superseded by IBody2::ISectionBySheet.
Obsolete. Superseded by [IBody2::ISectionBySheet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ISectionBySheet.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ISectionBySheet( _
   ByVal Sheet As Body, _
   ByVal NumMaxSections As System.Integer, _
   ByRef SectionedBodies As Body _
) As System.Integer
```

```

Dim instance As IBody
Dim Sheet As Body
Dim NumMaxSections As System.Integer
Dim SectionedBodies As Body
Dim value As System.Integer
 
value = instance.ISectionBySheet(Sheet, NumMaxSections, SectionedBodies)
```

```

System.int ISectionBySheet( 
   Body Sheet,
   System.int NumMaxSections,
   ref Body SectionedBodies
)
```

```

System.int ISectionBySheet( 
   Body^ Sheet,
   System.int NumMaxSections,
   Body^% SectionedBodies
) 
```

#### Parameters

*Sheet*

*NumMaxSections*

*SectionedBodies*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.md)  
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.md)
