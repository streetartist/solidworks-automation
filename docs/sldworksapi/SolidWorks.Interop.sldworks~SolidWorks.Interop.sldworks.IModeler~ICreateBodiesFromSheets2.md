# ICreateBodiesFromSheets2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodiesFromSheets2`

Sews sheets to make a sheet (surface) or solid bodies.
Sews sheets to make a sheet (surface) or solid bodies.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateBodiesFromSheets2( _
   ByVal NSheets As System.Integer, _
   ByRef Sheets As Body2, _
   ByVal Options As System.Integer, _
   ByVal KnittingTolerance As System.Double, _
   ByRef NResults As System.Integer, _
   ByRef Results As Body2 _
) As System.Integer
```

```

Dim instance As IModeler
Dim NSheets As System.Integer
Dim Sheets As Body2
Dim Options As System.Integer
Dim KnittingTolerance As System.Double
Dim NResults As System.Integer
Dim Results As Body2
Dim value As System.Integer
 
value = instance.ICreateBodiesFromSheets2(NSheets, Sheets, Options, KnittingTolerance, NResults, Results)
```

```

System.int ICreateBodiesFromSheets2( 
   System.int NSheets,
   ref Body2 Sheets,
   System.int Options,
   System.double KnittingTolerance,
   out System.int NResults,
   out Body2 Results
)
```

```

System.int ICreateBodiesFromSheets2( 
   System.int NSheets,
   Body2^% Sheets,
   System.int Options,
   System.double KnittingTolerance,
   [Out] System.int NResults,
   [Out] Body2^ Results
) 
```

#### Parameters

*NSheets*
:   Number of sheets

*Sheets*
:   Array containing the [sheets](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

*Options*
:   Type of body to create as defined by [swSheetSewingOption\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetSewingOption_e.html)

*KnittingTolerance*
:   Knitting tolerance

*NResults*
:   Number of sheet or solid bodies created

*Results*
:   Array of the sheet or solid [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

#### Return Value

Error as defined by [swSheetSewingError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetSewingError_e.html)

Remarks

It is safest to assume that the maximum number of bodies that can be returned by this method is the number of sheet input bodies. Your code should look like this:

aBodies = new IBody2\*[lNumSheetBodies];

hres = swModeler->ICreateBodiesFromSheets2(lNumSheetBodies, aSheetBodies, swSewToSheets, 1e-6, &lNumBodies, aBodies, &lErrors);

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::CreateBodiesFromSheets2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodiesFromSheets2.md)  
[IModeler::CreateBodyFromBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromBox.md)  
[IModeler::CreateBodyFromCone Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromCone.md)  
[IModeler::CreateBodyFromCyl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromCyl.md)  
[IModeler::CreateBodyFromFaces2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromFaces2.md)  
[IModeler::CreateBrepBody3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBrepBody3.md)  
[IModeler::CreateExtrudedBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateExtrudedBody.md)  
[IModeler::CreateSweptBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSweptBody.md)  
[IModeler::CreateWireBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateWireBody.md)  
[IModeler::ICreateBodyFromBox2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromBox2.md)  
[IModeler::ICreateBodyFromCone2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromCone2.md)  
[IModeler::ICreateBodyFromCyl2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromCyl2.md)  
[IModeler::ICreateBodyFromFaces3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromFaces3.md)  
[IModeler::ICreateBrepBody3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBrepBody3.md)  
[IModeler::ICreateWireBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateWireBody.md)
