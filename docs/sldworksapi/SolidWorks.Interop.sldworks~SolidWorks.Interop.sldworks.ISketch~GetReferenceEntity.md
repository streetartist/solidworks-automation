# GetReferenceEntity Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetReferenceEntity`

Gets the entity on which this sketch was created.
Gets the entity on which this sketch was created.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetReferenceEntity( _
   ByRef LEntityType As System.Integer _
) As System.Object
```

```

Dim instance As ISketch
Dim LEntityType As System.Integer
Dim value As System.Object
 
value = instance.GetReferenceEntity(LEntityType)
```

```

System.object GetReferenceEntity( 
   out System.int LEntityType
)
```

```

System.Object^ GetReferenceEntity( 
   [Out] System.int LEntityType
) 
```

#### Parameters

*LEntityType*
:   Entity type as defined in [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html) (only swSelFACES and swSelDATUMPLANES are valid values for this method)

#### Return Value

Either a [reference plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md) or a [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), depending on the value of lEntityType

Remarks

If the sketch resides on a face that is consumed by subsequent features, then this method returns NULL and swSelNOTHING. To get to the face, edit the sketch using [IModelDoc2::EditSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditSketch.md).

Example

[Get Plane On Which Sketch Created (VBA)](Get_Plane_on_which_Sketch_Created_Example_VB.htm)  
[Get Plane or Face for Sketch (VBA)](Get_Plane_or_Face_for_Sketch_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)
