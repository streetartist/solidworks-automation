# Select4 Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Select4`

Selects this component.
Selects this component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Select4( _
   ByVal Append As System.Boolean, _
   ByVal Data As SelectData, _
   ByVal ShowPopup As System.Boolean _
) As System.Boolean
```

```

Dim instance As IComponent2
Dim Append As System.Boolean
Dim Data As SelectData
Dim ShowPopup As System.Boolean
Dim value As System.Boolean
 
value = instance.Select4(Append, Data, ShowPopup)
```

```

System.bool Select4( 
   System.bool Append,
   SelectData Data,
   System.bool ShowPopup
)
```

```

System.bool Select4( 
   System.bool Append,
   SelectData^ Data,
   System.bool ShowPopup
) 
```

#### Parameters

*Append*
:   True appends the selection to the selection list, false replaces the selection list

*Data*
:   Pointer to the [ISelectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.md) object

*ShowPopup*
:   True to show shortcut menu, false to not

#### Return Value

True if the component is selected, false if not

Example

[Fire Notifications When Renaming Components (C#)](Fire_Notifications_When_Renaming_Components_Example_CSharp.htm)  
[Fire Notifications When Renaming Components (VB.NET)](Fire_Notifications_When_Renaming_Components_Example_VBNET.htm)  
[Fire Notifications When Renaming Components (VBA)](Fire_Notifications_When_Renaming_Components_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[ISelectionMgr::GetSelectedObjectsComponent3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsComponent3.md)  
[IModelDocExtension::SelectAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectAll.md)  
[IComponent2::DeSelect Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~DeSelect.md)
