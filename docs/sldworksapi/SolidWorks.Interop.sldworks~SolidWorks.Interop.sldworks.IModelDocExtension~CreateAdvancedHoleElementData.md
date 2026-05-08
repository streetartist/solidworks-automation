# CreateAdvancedHoleElementData Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateAdvancedHoleElementData`

Creates an Advanced Hole element data object of the specified type.
Creates an Advanced Hole element data object of the specified type.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateAdvancedHoleElementData( _
   ByVal ElmType As System.Integer _
) As System.Object
```

```

Dim instance As IModelDocExtension
Dim ElmType As System.Integer
Dim value As System.Object
 
value = instance.CreateAdvancedHoleElementData(ElmType)
```

```

System.object CreateAdvancedHoleElementData( 
   System.int ElmType
)
```

```

System.Object^ CreateAdvancedHoleElementData( 
   System.int ElmType
) 
```

#### Parameters

*ElmType*
:   Advanced Hole element type as defined in [swAdvWzdGeneralHoleTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAdvWzdGeneralHoleTypes_e.html)

#### Return Value

[IAdvancedHoleElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData.md) (see **Remarks**)

Remarks

After calling this method, use the IAdvancedHoleElementData object to get and set the properties common to all Advanced Hole elements. Cast the returned object using one of the following hole type-specific interfaces to set hole-specific properties:

- [ICounterboreElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICounterboreElementData.md)
- [ICountersinkElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICountersinkElementData.md)
- [IStraightElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData.md)
- [IStraightTapElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData.md)
- [ITaperedTapElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaperedTapElementData.md)

To create and Advanced Hole, see the [IFeatureManager::AdvancedHole](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AdvancedHole.md) Remarks.

Example

[Create Advanced Hole Feature (VBA)](Create_Advanced_Hole_Example_VB.htm)  
[Create Advanced Hole Feature (VB.NET)](Create_Advanced_Hole_Example_VBNET.htm)  
[Create Advanced Hole Feature (C#)](Create_Advanced_Hole_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
