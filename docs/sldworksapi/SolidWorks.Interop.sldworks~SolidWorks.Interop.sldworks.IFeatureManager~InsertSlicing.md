# InsertSlicing Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSlicing`

Creates and inserts slicing into the FeatureManager design tree.
Creates and inserts slicing into the FeatureManager design tree.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertSlicing( _
   ByVal SlicingData As System.Object, _
   ByRef Errors As System.Integer _
) As System.Object
```

```

Dim instance As IFeatureManager
Dim SlicingData As System.Object
Dim Errors As System.Integer
Dim value As System.Object
 
value = instance.InsertSlicing(SlicingData, Errors)
```

```

System.object InsertSlicing( 
   System.object SlicingData,
   out System.int Errors
)
```

```

System.Object^ InsertSlicing( 
   System.Object^ SlicingData,
   [Out] System.int Errors
) 
```

#### Parameters

*SlicingData*
:   [ISlicingData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.md) (see **Remarks**)

*Errors*
:   Errors as defined in [swInsertSlicingError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swInsertSlicingError_e.html)

#### Return Value

Array of sketch and reference plane objects

Remarks

This method invokes the Slicing tool. For more information, refer to **SOLIDWORKS Help > Parts and Features > Controlling Parts > Slicing Tool**.

Before calling this method:

1. Pre-select in the graphics area a planar entity (to create a linear pattern of slices) or a combination of a linear entity and a point entity (to create an angular pattern of slices whose axis is the linear entity).
2. Use [IFeatureManager::GetSlicingData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GetSlicingData.md) to get an ISlicingData object.
3. Set [ISlicingData::PlaneReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~PlaneReferences.md) if step 1 is not performed. Specify a planar entity or a combination of a linear entity and a point entity as specified in step 1.
4. Set other ISlicingData properties.
5. Populate SlicingData with the ISlicingData object.

After calling this method:

- Use the array of sketch and reference plane objects returned by this method to perform further work.
- If [ISlicingData::AddSlicingPlanesAndSketchesToFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~AddSlicingPlanesAndSketchesToFolder.md) was set to true, then a **Slice1** folder in the FeatureManager design tree is created containing the slicing planes and sketches. You can edit the slicing planes and sketches individually as needed.
- Delete the Slice1 folder and its contents to remove slicing from the model.

Example

See the [ISlicingData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
