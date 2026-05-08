# INote Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote`

Allows you to get standard note information.
Allows you to get standard note information.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface INote 
```

```

Dim instance As INote
```

```

public interface INote 
```

```

public interface class INote 
```

Remarks

**Important**: [Compound notes](ms-its:sldworksapiprogguide.chm::/Overview/Compound_Note.htm) are no longer creatable through the SOLIDWORKS user interface. As such, they are a legacy annotation type. SOLIDWORKS APIs that work on compound notes should only be used with legacy SOLIDWORKS files. [ISketchBlockDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.md) and [ISketchBlockInstance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.md) can be used to mimic the functionality of compound notes. See [Block Definitions and Block Instances](ms-its:sldworksapiprogguide.chm::/Overview/Block_Definitions_and_Block_Instances.htm).

Example

[Get Notes from New or Existing Title Block (C#)](Get_Notes_from_New_or_Existing_Title_Block_Example_CSharp.htm)  
[Get Notes from New or Existing Title Block (VB.NET)](Get_Notes_from_New_or_Existing_Title_Block_Example_VBNET.htm)  
[Get Notes from New or Existing Title Block (VBA)](Get_Notes_from_New_or_Existing_Title_Block_Example_VB.htm)  
[Anchor a Note (VBA)](Anchor_a_Note_Example_VB.htm)  
[Anchor a Note (VB.NET)](Anchor_a_Note_Example_VBNET.htm)  
[Anchor a Note (C#)](Anchor_a_Note_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IModelDoc2::InsertNewNote3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertNewNote3.md)  
[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)
