# Select4 Method (IEntity)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~Select4`

Selects an entity and marks it.
Selects an entity and marks it.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Select4( _
   ByVal Append As System.Boolean, _
   ByVal Data As SelectData _
) As System.Boolean
```

```

Dim instance As IEntity
Dim Append As System.Boolean
Dim Data As SelectData
Dim value As System.Boolean
 
value = instance.Select4(Append, Data)
```

```

System.bool Select4( 
   System.bool Append,
   SelectData Data
)
```

```

System.bool Select4( 
   System.bool Append,
   SelectData^ Data
) 
```

#### Parameters

*Append*
:   True appends the entity to the selection list, false replaces the selection list with this entity

*Data*
:   Pointer to the [ISelectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.md) object

#### Return Value

True if the selection is successful, false if not

Remarks

When you use this method, selection behaves differently depending on the command state of SOLIDWORKS. One case is when SOLIDWORKS is running a command that has a PropertyManager associated with a selection list box (for example, a feature creation command such as Insert Fillet). The selection behavior in this case is:

- Selecting a new entity appends it to the selection list.

- or -

- Selecting an entity that is already selected deselects the entity.

SOLIDWORKS ignores the Append argument because the selection is always appended to the selection list.

 

The second case is when there is no command running, which is the default state of SOLIDWORKS.

You can use this method only with [IEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md) objects that you get from the active document. For example, if Assembly1 is the active document when you call this method, then you must get the entity directly from the Assembly1 document. You can do this using items in the selection list (for example, [ISelectionMgr::GetSelectedObject6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.md)) or you can traverse the body of an assembly component (for example, [IComponent2::GetBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetBody.md) and [IBody2::GetFirstFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFirstFace.md)). You cannot obtain the entity from the underlying part document (for example, [IComponent2::GetModelDoc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetModelDoc.md) or [IBody2::GetFirstFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFirstFace.md)).

You can use this method to select features. In Visual C++, you must first get the [IEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md) interface from the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object.

Example

[Check Interference Using IAssemblyDoc::ToolsCheckInterference2 (VBA)](Check_Interference_using_AssemblyDoc_ToolsCheckInterference2_Example_VB.htm)  
[Get Faces Associated with Feature (VBA)](Get_Faces_Associated_with_Feature_Example_VB.htm)  
[Get Reference Point Data (VBA)](Get_Reference_Point_Data_Example_VB.htm)  
[Get Visible Components and Entities in Drawing View (VBA)](Get_Visible_Components_and_Entities_in_Drawing_View_Example_VB.htm)  
[Select Loop of Edges (VBA)](Select_Loop_of_Edges_Example_VB_.htm)  
[Use Safe Entity (VBA)](Use_Safe_Entity_Example_VB.htm)  
[Get Offset Surface Data (C#)](Get_Offset_Surface_Data_Example_CSharp.htm)  
[Get Offset Surface Data (VB.NET)](Get_Offset_Surface_Data_Example_VBNET.htm)  
[Get Offset Surface Data (VBA)](Get_Offset_Surface_Data_Example_VB.htm)  
[Select Edges of All Holes on Face (C#)](Select_Edges_of_All_Holes_on_Face_Example_CSharp.htm)  
[Select Edges of All Holes on Face (VB.NET)](Select_Edges_of_All_Holes_on_Face_Example_VBNET.htm)  
[Select Edges of All Holes on Face (VBA)](Select_Edges_of_All_Holes_on_Face_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEntity Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md)  
[IEntity Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity_members.md)
