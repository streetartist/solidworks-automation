# InsertNewPart2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertNewPart2`

Inserts a new part on the specified face or plane.
Inserts a new part on the specified face or plane.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertNewPart2( _
   ByVal FilePathIn As System.String, _
   ByVal Face_or_Plane_to_select As System.Object _
) As System.Integer
```

```

Dim instance As IAssemblyDoc
Dim FilePathIn As System.String
Dim Face_or_Plane_to_select As System.Object
Dim value As System.Integer
 
value = instance.InsertNewPart2(FilePathIn, Face_or_Plane_to_select)
```

```

System.int InsertNewPart2( 
   System.string FilePathIn,
   System.object Face_or_Plane_to_select
)
```

```

System.int InsertNewPart2( 
   System.String^ FilePathIn,
   System.Object^ Face_or_Plane_to_select
) 
```

#### Parameters

*FilePathIn*
:   Path and filename for the new part

*Face\_or\_Plane\_to\_select*
:   [Face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) or [reference plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md) where to insert the new part

#### Return Value

Error code as defined by [swInsertNewPartErrorCode\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInsertNewPartErrorCode_e.html)

Remarks

The Face\_or\_Plane\_to\_select argument can be a [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) or [reference plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md), which means that you have to call [IFeature::GetSpecificFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.md) first.

Example

[Insert Join Feature (C#)](Insert_Join_Feature_Example_CSharp.htm)  
[Insert Join Feature (VB.NET)](Insert_Join_Feature_Example_VBNET.htm)  
[Insert Join Feature (VBA)](Insert_Join_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)
