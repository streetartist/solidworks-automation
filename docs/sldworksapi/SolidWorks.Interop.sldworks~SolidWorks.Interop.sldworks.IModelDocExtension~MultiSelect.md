# MultiSelect Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~MultiSelect`

Obsolete. Superseded by IModelDocExtension::MultiSelect2.
Obsolete. Superseded by [IModelDocExtension::MultiSelect2.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~MultiSelect2.md)

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function MultiSelect( _
   ByVal Objects As System.Object, _
   ByVal AppendFlag As System.Boolean, _
   ByVal Data As System.Object _
) As System.Integer
```

```

Dim instance As IModelDocExtension
Dim Objects As System.Object
Dim AppendFlag As System.Boolean
Dim Data As System.Object
Dim value As System.Integer
 
value = instance.MultiSelect(Objects, AppendFlag, Data)
```

```

System.int MultiSelect( 
   System.object Objects,
   System.bool AppendFlag,
   System.object Data
)
```

```

System.int MultiSelect( 
   System.Object^ Objects,
   System.bool AppendFlag,
   System.Object^ Data
) 
```

#### Parameters

*Objects*
:   Array of selectable objects:

    - can be the same type of objects (e.g., an array of faces or an array of edges) or different types of objects (e.g., an array of entities of faces and edges )
    - if an object is not selected, then it is ignored

*AppendFlag*
:   True to append the objects to the selection list, false to replace the current selection list with these objects

*Data*
:   [ISelectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.md) object, Nothing, or null

#### Return Value

Number of objects selected in the model

Remarks

If this now obsolete method is used to populate a selection box in a PropertyManager page, then [IPropertyManagerPage2Handler9::OnSubmitSelection](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler9~OnSubmitSelection.md) only fires when set to true and [ISelectData::Mark](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData~Mark.md) is set to 0.

Use [IModelDocExtension::MultiSelect2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~MultiSelect2.md) if you need IPropertyManagerPage2Handler9::OnSubmitSelection to fire when set to true and ISelectData::Mark is set to either a 0 or non-0 value.

The [Callout](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData~Callout.md) property of the [ISelectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.md) object is not used by this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::IModelDocSelectByID2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IMultiSelect.md)  
[IModelDocExtension::SelectByID2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md)  
[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.md)  
[IModelDocExtension::SelectAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectAll.md)
