# SetAddToDB Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetAddToDB`

Obsolete. Superseded by ISketchManager::AddToDB.
Obsolete. Superseded by [ISketchManager::AddToDB](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~AddToDB.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetAddToDB( _
   ByVal Setting As System.Boolean _
) 
```

```

Dim instance As IModelDoc2
Dim Setting As System.Boolean
 
instance.SetAddToDB(Setting)
```

```

void SetAddToDB( 
   System.bool Setting
)
```

```

void SetAddToDB( 
   System.bool Setting
) 
```

#### Parameters

*Setting*
:   True to add items directly to the SOLIDWORKS database, false if not

Remarks

One of the benefits of adding sketch entities directly to the database is that you can avoid grid and entity snapping. For example, if you create a sketch line whose endpoint is near another entity or near a grid point, the new line endpoint snaps to the other item or grid point. Setting ModelDoc2::SetAddToDB to True avoids this behavior during sketch entity creation.

IModelDoc2::SetAddToDb and [IModelDoc2::SetDisplayWhenAdded](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetDisplayWhenAdded.md) also increase performance during sketch entity creation. IModelDoc2::SetDisplayWhenAdded requires that IModelDoc2::SetAddToDB is True.

If you want to constrain all the sketch entities after creation, use [ISketch::ConstrainAll](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~ConstrainAll.md).

After setting IModelDoc2::SetAddToDB to True, you must set it back to false to restore SOLIDWORKS to its normal operating mode.

Example

[Tessellate a Body (C#)](Tessellate_a_Body_Example_CSharp.htm)  
[Calculate Closest Distance Between Faces (VBA)](Calculate_Closest_Distance_Between_Faces_Example_VB.htm)  
[Calculate Closest Distance Between Model Components (VBA)](Calculate_Closest_Distance_Between_Model_Components_Example_VB.htm)  
[Create Plane Thru 3 Points In-context (VBA)](Create_Plane_Thru_3_Points_In-context_Example_VB.htm)  
[Get Intersecting Face and Edge (VBA)](Get_Intersecting_Face_and_Edge_Example_VB.htm)  
[Get Intersecting Faces (VBA)](Get_Intersecting_Faces_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::GetAddToDB Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetAddToDB.md)
