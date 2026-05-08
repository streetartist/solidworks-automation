# ISectionBySheet Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ISectionBySheet`

Sections a body using a sheet (surface) body.
Sections a body using a sheet (surface) body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ISectionBySheet( _
   ByVal Sheet As Body2, _
   ByVal NumMaxSections As System.Integer, _
   ByRef SectionedBodies As Body2 _
) As System.Integer
```

```

Dim instance As IBody2
Dim Sheet As Body2
Dim NumMaxSections As System.Integer
Dim SectionedBodies As Body2
Dim value As System.Integer
 
value = instance.ISectionBySheet(Sheet, NumMaxSections, SectionedBodies)
```

```

System.int ISectionBySheet( 
   Body2 Sheet,
   System.int NumMaxSections,
   ref Body2 SectionedBodies
)
```

```

System.int ISectionBySheet( 
   Body2^ Sheet,
   System.int NumMaxSections,
   Body2^% SectionedBodies
) 
```

#### Parameters

*Sheet*
:   Pointer to the sheet body used to perform the section

*NumMaxSections*
:   Maximum number of sections to create

*SectionedBodies*
:   Pointer to an array of [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) created during the section operation

#### Return Value

Number of bodies created during the operation

Remarks

Before using this method, [make a copy of the body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Copy.md) because the sheet body becomes invalid after using this method. COM applications should release all bodies after calling this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)
