# GetAnnotation Method (ICenterMark)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~GetAnnotation`

Gets the annotation for this center mark.
Gets the annotation for this center mark.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAnnotation() As Annotation
```

```

Dim instance As ICenterMark
Dim value As Annotation
 
value = instance.GetAnnotation()
```

```

Annotation GetAnnotation()
```

```

Annotation^ GetAnnotation(); 
```

#### Return Value

[Annotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md) object

Remarks

This method returns null or nothing for center marks created as features (earlier style of center marks). See [ICenterMark](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.md) for details about the old and new style center marks. See SOLIDWORKS Help for details about center marks.

For example, if [ISelectionMgr::GetSelectedObjectType3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectType3.md) equals swSelCENTERMARKS, then ICenterMark::GetAnnotation equals null or nothing. But, if ISelectionMgr::GetSelectedObjectType3 equals swSelCENTERMARKSYMS, then ICenterMark::GetAnnotation points to the IAnnotation object.

Example

[Get Annotation Object (VBA)](Get_Annotation_Object_Example_VB.htm)  
[Get Annotation Object (VB.NET)](Get_Annotation_Object_Example_VBNET.htm)  
[Get Annotation Object (C#)](Get_Annotation_Object_Example_CSharp.htm)  
[Select All Center Marks (C#)](Select_All_Center_Marks_Example_CSharp.htm)  
[Select All Center Marks (VB.NET)](Select_All_Center_Marks_Example_VBNET.htm)  
[Select All Center Marks (VBA)](Select_All_Center_Marks_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICenterMark Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.md)  
[ICenterMark Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark_members.md)
