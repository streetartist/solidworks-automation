# DeleteSelection2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteSelection2`

Deletes the selected items, with the option to delete absorbed features, child features, or both.
Deletes the selected items, with the option to delete absorbed features, child features, or both.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DeleteSelection2( _
   ByVal DeleteOptions As System.Integer _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim DeleteOptions As System.Integer
Dim value As System.Boolean
 
value = instance.DeleteSelection2(DeleteOptions)
```

```

System.bool DeleteSelection2( 
   System.int DeleteOptions
)
```

```

System.bool DeleteSelection2( 
   System.int DeleteOptions
) 
```

#### Parameters

*DeleteOptions*
:   Options as defined in [swDeleteSelectionOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDeleteSelectionOptions_e.html)

#### Return Value

True if the selected item is deleted, false if not

Remarks

This method does not ask the user to confirm the deletion.

Example

[Create Extruded Thin Feature (VBA)](Create_Extruded_Thin_Feature_Example_VB.htm)  
[Delete Selected Feature (VBA)](Delete_Selected_Feature_Example_VB.htm)  
[Undo Feature and Fire Undo Post-Notify Event (VBA)](Undo_Feature_and_Fire_Undo_Post-Notify_Event_Example_VB.htm)  
[Undo Feature and Fire Undo Post Notify Event (VB.NET)](Undo_Feature_and_Fire_Undo_Post-Notify_Event_Example_VBNET.htm)  
[Undo Feature and Fire Undo Post-Notify Event (C#)](Undo_Feature_and_Fire_Undo_Post-Notify_Event_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IAssemblyDoc::DeleteSelections Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~DeleteSelections.md)  
[IModel2::EditDelete Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditDelete.md)
