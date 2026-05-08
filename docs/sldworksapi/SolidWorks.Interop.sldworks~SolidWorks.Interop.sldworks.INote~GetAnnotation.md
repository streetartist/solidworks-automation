# GetAnnotation Method (INote)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetAnnotation`

Gets the annotation for this specific note.
Gets the annotation for this specific note.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAnnotation() As System.Object
```

```

Dim instance As INote
Dim value As System.Object
 
value = instance.GetAnnotation()
```

```

System.object GetAnnotation()
```

```

System.Object^ GetAnnotation(); 
```

#### Return Value

[Annotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)

Remarks

This method obtains the owning [IAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md) object for this [INote](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md) object. The IAnnotation object is a higher-level object that contains methods that are general to all types of annotations.

Example

[Get All Notes in Drawing Template (VBA)](Get_All_Notes_in_Drawing_Template_Example_VB.htm)  
[Insert Note (VBA)](Insert_a_Note_Example_VB.htm)  
[Insert Autoballoons (VBA)](Insert_Autoballoons_Example_VB_AutoBalloon2_VB.htm)  
[Set BOM Balloon Text (VBA)](Set_BOM_Balloon_Example_VB.htm)  
[Get Annotation Object (VBA)](Get_Annotation_Object_Example_VB.htm)  
[Get Annotation Object (VB.NET)](Get_Annotation_Object_Example_VBNET.htm)  
[Get Annotation Object (C#)](Get_Annotation_Object_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)  
[INote::IGetAnnotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetAnnotation.md)
