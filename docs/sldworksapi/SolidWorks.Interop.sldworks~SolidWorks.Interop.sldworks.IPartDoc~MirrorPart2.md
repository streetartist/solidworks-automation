# MirrorPart2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MirrorPart2`

Creates a new part document that mirrors this part about a selected reference plane or planar face.
Creates a new part document that mirrors this part about a selected reference plane or planar face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function MirrorPart2( _
   ByVal BreakLink As System.Boolean, _
   ByVal Options As System.Integer, _
   ByRef ResultPart As ModelDoc2 _
) As Feature
```

```

Dim instance As IPartDoc
Dim BreakLink As System.Boolean
Dim Options As System.Integer
Dim ResultPart As ModelDoc2
Dim value As Feature
 
value = instance.MirrorPart2(BreakLink, Options, ResultPart)
```

```

Feature MirrorPart2( 
   System.bool BreakLink,
   System.int Options,
   out ModelDoc2 ResultPart
)
```

```

Feature^ MirrorPart2( 
   System.bool BreakLink,
   System.int Options,
   [Out] ModelDoc2^ ResultPart
) 
```

#### Parameters

*BreakLink*
:   True to break the link to the original part, false to not

*Options*
:   Insertion options as defined in [swMirrorPartOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMirrorPartOptions_e.html)

*ResultPart*
:   [IModelDoc2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

Before calling this method, you must select a reference plane or planar face about which to mirror this part.

Example

[Get Mirror Part Information (VBA)](Get_Mirror_Part_Information_Example_VB.htm)  
[Get Mirror Part Information (VB.NET)](Get_Mirror_Part_Information_Example_VBNET.htm)  
[Get Mirror Part Information (C#)](Get_Mirror_Part_Information_Example_CSharp.htm)  
[Mirror Sheet-metal Part (C#)](Mirror_Sheet-metal_Part_Example_CSharp.htm)  
[Mirror Sheet-metal Part (VB.NET)](Mirror_Sheet-metal_Part_Example_VBNET.htm)  
[Mirror Sheet-metal Part (VBA)](Mirror_Sheet-metal_Part_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IMirrorPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData.md)  
[IPartDoc::InsertMirrorAll Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~InsertMirrorAll.md)  
[IPartDoc::MirrorFeature Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MirrorFeature.md)  
[IFeatureManager::InsertMirrorFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMirrorFeature2.md)
