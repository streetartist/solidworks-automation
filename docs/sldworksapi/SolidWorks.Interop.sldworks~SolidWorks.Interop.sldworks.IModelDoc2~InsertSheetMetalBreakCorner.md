# InsertSheetMetalBreakCorner Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSheetMetalBreakCorner`

Inserts a break corner into a sheet metal part.
Inserts a break corner into a sheet metal part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertSheetMetalBreakCorner( _
   ByVal Type As System.Integer, _
   ByVal Distance As System.Double _
) 
```

```

Dim instance As IModelDoc2
Dim Type As System.Integer
Dim Distance As System.Double
 
instance.InsertSheetMetalBreakCorner(Type, Distance)
```

```

void InsertSheetMetalBreakCorner( 
   System.int Type,
   System.double Distance
)
```

```

void InsertSheetMetalBreakCorner( 
   System.int Type,
   System.double Distance
) 
```

#### Parameters

*Type*
:   Corner type as defined in [swBreakCornerTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBreakCornerTypes_e.html)

*Distance*
:   Distance to break from corner

Example

[Modify Break Corner Feature (C#)](Modify_Break_Corner_Feature_Example_CSharp.htm)  
[Modify Break Corner Feature (VB.NET)](Modify_Break_Corner_Feature_Example_VBNET.htm)  
[Modify Break Corner Feature (VBA)](Modify_Break_Corner_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IBreakCornerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData.md)
