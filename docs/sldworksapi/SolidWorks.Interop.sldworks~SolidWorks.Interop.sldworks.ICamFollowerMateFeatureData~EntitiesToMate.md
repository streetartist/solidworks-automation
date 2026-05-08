# EntitiesToMate Property (ICamFollowerMateFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamFollowerMateFeatureData~EntitiesToMate`

Gets or sets the entities to mate in this cam-follower mate.
Gets or sets the entities to mate in this cam-follower mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EntitiesToMate( _
   ByVal EntityType As System.Integer _
) As System.Object
```

```

Dim instance As ICamFollowerMateFeatureData
Dim EntityType As System.Integer
Dim value As System.Object
 
instance.EntitiesToMate(EntityType) = value
 
value = instance.EntitiesToMate(EntityType)
```

```

System.object EntitiesToMate( 
   System.int EntityType
) {get; set;}
```

```

property System.Object^ EntitiesToMate {
   System.Object^ get(System.int EntityType);
   void set (System.int EntityType, System.Object^ value);
}
```

#### Parameters

*EntityType*
:   Type of cam entity to mate as defined in [swCamMateEntityType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCamMateEntityType_e.html) (see **Remarks**)

#### Property Value

Array of entities to mate (see **Remarks**)

Remarks

Use this property with EntityType set to swCamMateEntityType\_e.:

- CamPath, to get or set the cam [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) to mate.
- CamFollower, to get or set the cam-follower face or [vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md) to mate.

Instead of specifying this property, you can use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to pre-select the entities to mate using Mark = 1 for the cam face and Mark = 8 for the cam follower face or vertex. You can pre-select mate entities during mate creation, but not during mate editing.

Example

See the [ICamFollowerMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamFollowerMateFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICamFollowerMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamFollowerMateFeatureData.md)  
[ICamFollowerMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamFollowerMateFeatureData_members.md)
