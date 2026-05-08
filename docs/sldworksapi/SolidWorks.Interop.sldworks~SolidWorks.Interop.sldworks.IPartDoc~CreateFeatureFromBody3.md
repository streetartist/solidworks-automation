# CreateFeatureFromBody3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~CreateFeatureFromBody3`

Creates a new imported feature from the specified temporary body.
Creates a new imported feature from the specified temporary body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateFeatureFromBody3( _
   ByVal Body As System.Object, _
   ByVal MakeRefSurface As System.Boolean, _
   ByVal Options As System.Integer _
) As System.Object
```

```

Dim instance As IPartDoc
Dim Body As System.Object
Dim MakeRefSurface As System.Boolean
Dim Options As System.Integer
Dim value As System.Object
 
value = instance.CreateFeatureFromBody3(Body, MakeRefSurface, Options)
```

```

System.object CreateFeatureFromBody3( 
   System.object Body,
   System.bool MakeRefSurface,
   System.int Options
)
```

```

System.Object^ CreateFeatureFromBody3( 
   System.Object^ Body,
   System.bool MakeRefSurface,
   System.int Options
) 
```

#### Parameters

*Body*
:   Temporary [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

*MakeRefSurface*
:   If the body cannot be knitted to a solid or if a solid body already exists in this model, then True creates a reference surface feature

*Options*
:   Options as defined in [swCreateFeatureBodyOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCreateFeatureBodyOpts_e.html)

#### Return Value

Newly created imported [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) or Nothing or NULL if the operation fails

Remarks

This method is intended to be the final call in a knitting operation. The body that results from your knitting efforts can be converted into an imported body feature in the SOLIDWORKS model. This method is not limited to body objects obtained from knitting operations.

This method allows the application to decide how much additional work needs to be done to the model before creating the feature. The options listed in the swCreateFeatureBodyOpts\_e enumeration can be OR'd together to provide additional checking or simplification of the model. If you specify swCreateFeatureBodySimplify for Options, then swCreateFeatureBodyCheck is implied.

If the application passes 0 for the options argument, then the options are disabled and the model is passed without any checking. If so, it is up to the application to ensure that the model is a valid model.

If this method fails, the error might be caused by creating a sheet (surface) body from a multiple shells body. If so, replace this method with [IPartDoc::CreateSurfaceFeatureFromBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~CreateSurfaceFeatureFromBody.md) or [IPartDoc::ICreateSurfaceFeatureFromBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ICreateSurfaceFeatureFromBody.md).

Example

[Combine Assembly Components Into Part (VBA)](Combine_Assembly_Components_into_Part_Example_VB.htm)  
[Delete Faces (VBA)](Delete_Faces_Example_VB.htm)  
[Get Differences Between Parts (VBA)](Get_Differences_Between_Parts_Example_VB.htm)  
[Get Sectioned Bodies (VBA)](Get_Sectioned_Bodies_Example_VB.htm)  
[Save Rollbacked Part as Parasolid File (VBA)](Save_Roll_Backed_Part_as_Parasolid_File_Example_VB.htm)  
[Create Sheet Body From Faces and Feature From Sheet Body (VBA)](Create_Sheet_Body_From_Faces_and_Feature_from_Sheet_Body_Example_VB.htm)  
[Process Body (C#)](Process_Body_Example_CSharp.htm)  
[Process Body (VB.NET)](Process_Body_Example_VBNET.htm)  
[Process Body (VBA)](Process_Body_Example_VB.htm)  
[Delete Blended Faces (C#)](Delete_Blended_Faces_Example_CSharp.htm)  
[Delete Blended Faces (VB.NET)](Delete_Blended_Faces_Example_VBNET.htm)  
[Delete Blended Faces (VBA)](Delete_Blended_Faces_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IPartDoc::ICreateFeatureFromBody4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ICreateFeatureFromBody4.md)
