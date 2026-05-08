# InsertSheetMetalMiterFlange Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertSheetMetalMiterFlange`

Obsolete. Superseded by IModelDoc2::InsertSheetMetalMiterFlange.
Obsolete. Superseded by [IModelDoc2::InsertSheetMetalMiterFlange](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSheetMetalMiterFlange.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertSheetMetalMiterFlange( _
   ByVal UseReliefRatio As System.Boolean, _
   ByVal UseDefaultGap As System.Boolean, _
   ByVal UseAutoRelief As System.Boolean, _
   ByVal GlobalRadius As System.Double, _
   ByVal RipGap As System.Double, _
   ByVal AutoReliefRatio As System.Double, _
   ByVal AutoReliefWidth As System.Double, _
   ByVal AutoReliefDepth As System.Double, _
   ByVal ReliefType As System.Integer, _
   ByVal RipLocation As System.Integer, _
   ByVal TrimSideBends As System.Boolean _
) 
```

```

Dim instance As IModelDoc
Dim UseReliefRatio As System.Boolean
Dim UseDefaultGap As System.Boolean
Dim UseAutoRelief As System.Boolean
Dim GlobalRadius As System.Double
Dim RipGap As System.Double
Dim AutoReliefRatio As System.Double
Dim AutoReliefWidth As System.Double
Dim AutoReliefDepth As System.Double
Dim ReliefType As System.Integer
Dim RipLocation As System.Integer
Dim TrimSideBends As System.Boolean
 
instance.InsertSheetMetalMiterFlange(UseReliefRatio, UseDefaultGap, UseAutoRelief, GlobalRadius, RipGap, AutoReliefRatio, AutoReliefWidth, AutoReliefDepth, ReliefType, RipLocation, TrimSideBends)
```

```

void InsertSheetMetalMiterFlange( 
   System.bool UseReliefRatio,
   System.bool UseDefaultGap,
   System.bool UseAutoRelief,
   System.double GlobalRadius,
   System.double RipGap,
   System.double AutoReliefRatio,
   System.double AutoReliefWidth,
   System.double AutoReliefDepth,
   System.int ReliefType,
   System.int RipLocation,
   System.bool TrimSideBends
)
```

```

void InsertSheetMetalMiterFlange( 
   System.bool UseReliefRatio,
   System.bool UseDefaultGap,
   System.bool UseAutoRelief,
   System.double GlobalRadius,
   System.double RipGap,
   System.double AutoReliefRatio,
   System.double AutoReliefWidth,
   System.double AutoReliefDepth,
   System.int ReliefType,
   System.int RipLocation,
   System.bool TrimSideBends
) 
```

#### Parameters

*UseReliefRatio*

*UseDefaultGap*

*UseAutoRelief*

*GlobalRadius*

*RipGap*

*AutoReliefRatio*

*AutoReliefWidth*

*AutoReliefDepth*

*ReliefType*

*RipLocation*

*TrimSideBends*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
