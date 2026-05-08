# GetSelectionSetByName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSetFolder~GetSelectionSetByName`

Gets the specified selection set.
Gets the specified selection set.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSelectionSetByName( _
   ByVal Name As System.String _
) As System.Object
```

```

Dim instance As ISelectionSetFolder
Dim Name As System.String
Dim value As System.Object
 
value = instance.GetSelectionSetByName(Name)
```

```

System.object GetSelectionSetByName( 
   System.string Name
)
```

```

System.Object^ GetSelectionSetByName( 
   System.String^ Name
) 
```

#### Parameters

*Name*
:   Name of the selection set

#### Return Value

[Selection set](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet.md)

Remarks

To get the name of a selection folder to pass to this method, you can traverse [items in the FeatureManager design tree](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem.md). See the examples.

Example

[Get Objects in Selection Set (C#)](Get_Objects_in_Selection_Set_Example_CSharp.htm)  
[Get Objects in Selection Set (VB.NET)](Get_Objects_in_Selection_Set_Example_VBNET.htm)  
[Get Objects in Selection Set (VBA)](Get_Objects_in_Selection_Set_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISelectionSetFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSetFolder.md)  
[ISelectionSetFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSetFolder_members.md)  
[ISelectionSetFolder::GetSelectionSets Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSetFolder~GetSelectionSets.md)
