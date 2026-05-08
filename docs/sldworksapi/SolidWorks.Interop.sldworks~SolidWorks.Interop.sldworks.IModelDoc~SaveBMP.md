# SaveBMP Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SaveBMP`

Obsolete. Superseded by IModelDoc2::SaveBMP.
Obsolete. Superseded by [IModelDoc2::SaveBMP](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SaveBMP.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SaveBMP( _
   ByVal FileNameIn As System.String, _
   ByVal WidthIn As System.Integer, _
   ByVal HeightIn As System.Integer _
) As System.Boolean
```

```

Dim instance As IModelDoc
Dim FileNameIn As System.String
Dim WidthIn As System.Integer
Dim HeightIn As System.Integer
Dim value As System.Boolean
 
value = instance.SaveBMP(FileNameIn, WidthIn, HeightIn)
```

```

System.bool SaveBMP( 
   System.string FileNameIn,
   System.int WidthIn,
   System.int HeightIn
)
```

```

System.bool SaveBMP( 
   System.String^ FileNameIn,
   System.int WidthIn,
   System.int HeightIn
) 
```

#### Parameters

*FileNameIn*

*WidthIn*

*HeightIn*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
