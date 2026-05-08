# Select3 Method (IAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~Select3`

Selects this annotation and marks it.
Selects this annotation and marks it.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Select3( _
   ByVal Append As System.Boolean, _
   ByVal Data As SelectData _
) As System.Boolean
```

```

Dim instance As IAnnotation
Dim Append As System.Boolean
Dim Data As SelectData
Dim value As System.Boolean
 
value = instance.Select3(Append, Data)
```

```

System.bool Select3( 
   System.bool Append,
   SelectData Data
)
```

```

System.bool Select3( 
   System.bool Append,
   SelectData^ Data
) 
```

#### Parameters

*Append*
:   True appends this selection to the current selection list, false replaces the current selection list with this selection

*Data*
:   Pointer to the [ISelectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.md) object

#### Return Value

True if the annotation was selected, false if not

Example

[Get Corresponding Note in Assembly (VBA)](Get_Corresponding_Note_in_Assembly_Example_VB.htm)  
[Get Corresponding Note in Part (VBA)](Get_Corresponding_Note_in_Part_Example_VB.htm)  
[Insert Model Annotations (C#)](Insert_Model_Annotations_Example_CSharp.htm)  
[Insert Model Annotations (VB.NET)](Insert_Model_Annotations_Example_VBNET.htm)  
[Insert Model Annotations (VBA)](Insert_Model_Annotations_Example_VB.htm)  
[Select All Center Marks (C#)](Select_All_Center_Marks_Example_CSharp.htm)  
[Select All Center Marks (VB.NET)](Select_All_Center_Marks_Example_VBNET.htm)  
[Select All Center Marks (VBA)](Select_All_Center_Marks_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)
